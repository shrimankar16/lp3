'use strict';

/**
 * Test File — Hyperledger Composer Business Network
 * Tests the Trade transaction logic using an embedded connector
 * (no actual Fabric network needed to run these tests)
 */

const AdminConnection   = require('composer-admin').AdminConnection;
const BusinessNetworkConnection = require('composer-client').BusinessNetworkConnection;
const BusinessNetworkDefinition = require('composer-common').BusinessNetworkDefinition;
const IdCard = require('composer-common').IdCard;
const MemoryCardStore = require('composer-common').MemoryCardStore;

const path = require('path');

// Chai is the assertion library used for test checks
const chai   = require('chai');
const expect = chai.expect;
chai.use(require('chai-as-promised'));

// Network and participant details used across tests
const NS         = 'org.example.trading';
const cardStore  = new MemoryCardStore();

let adminConnection;
let businessNetworkConnection;
let factory;

/**
 * Setup — runs before all tests
 * Creates an admin connection and deploys the business network
 * into an in-memory (embedded) connector.
 */
before(async () => {
    // Create an admin connection using the in-memory card store
    adminConnection = new AdminConnection({ cardStore });

    // Create and import an admin identity card
    const adminCardName = 'admin@trade-network';
    let metadata = {
        userName: 'admin',
        enrollmentSecret: 'adminpw',
        roles: ['PeerAdmin', 'ChannelAdmin']
    };
    const connectionProfile = { name: 'embedded', 'x-type': 'embedded' };
    const adminCard = new IdCard(metadata, connectionProfile);

    await adminConnection.importCard(adminCardName, adminCard);
    await adminConnection.connect(adminCardName);

    // Load the business network definition from the project root
    const businessNetworkDefinition = await BusinessNetworkDefinition.fromDirectory(
        path.resolve(__dirname, '..')
    );

    // Deploy the network to the embedded connector
    await adminConnection.deploy(businessNetworkDefinition);

    // Create a client connection and connect
    businessNetworkConnection = new BusinessNetworkConnection({ cardStore });
    await businessNetworkConnection.connect(adminCardName);

    // Get the factory to create new model instances
    factory = businessNetworkConnection.getBusinessNetwork().getFactory();
});

/**
 * Test Suite: Trade Transaction
 */
describe('Trade Network', () => {

    /**
     * Test 1: Create two Trader participants and a Commodity asset,
     * then submit a Trade transaction and verify ownership changes.
     */
    it('should change commodity owner after a trade', async () => {

        // ── Create Trader 1 (Seller) ──────────────────────
        const seller = factory.newResource(NS, 'Trader', 'TRADER1');
        seller.firstName = 'Alice';
        seller.lastName  = 'Smith';

        // ── Create Trader 2 (Buyer) ───────────────────────
        const buyer = factory.newResource(NS, 'Trader', 'TRADER2');
        buyer.firstName = 'Bob';
        buyer.lastName  = 'Jones';

        // Add both traders to the participant registry on the ledger
        const traderRegistry = await businessNetworkConnection.getParticipantRegistry(NS + '.Trader');
        await traderRegistry.addAll([seller, buyer]);

        // ── Create a Commodity owned by Trader 1 ─────────
        const commodity = factory.newResource(NS, 'Commodity', 'WHEAT');
        commodity.description  = 'Premium Wheat';
        commodity.mainExchange = 'Chicago';
        commodity.quantity     = 500.0;
        // Set owner as a relationship to Trader1
        commodity.owner = factory.newRelationship(NS, 'Trader', 'TRADER1');

        // Add the commodity to the asset registry on the ledger
        const commodityRegistry = await businessNetworkConnection.getAssetRegistry(NS + '.Commodity');
        await commodityRegistry.add(commodity);

        // ── Submit a Trade Transaction ────────────────────
        const trade = factory.newTransaction(NS, 'Trade');
        // The commodity being traded
        trade.commodity = factory.newRelationship(NS, 'Commodity', 'WHEAT');
        // The new owner after the trade
        trade.newOwner  = factory.newRelationship(NS, 'Trader', 'TRADER2');

        await businessNetworkConnection.submitTransaction(trade);

        // ── Verify Ownership Changed ──────────────────────
        // Re-fetch the commodity from the ledger
        const updatedCommodity = await commodityRegistry.get('WHEAT');

        // The commodity's owner should now be TRADER2 (Bob Jones)
        expect(updatedCommodity.owner.getIdentifier()).to.equal('TRADER2');
        console.log('✓ Trade successful: WHEAT ownership transferred from TRADER1 to TRADER2');
    });

    /**
     * Test 2: Verify initial commodity state before any trades
     */
    it('should have correct initial commodity quantity', async () => {
        const commodityRegistry = await businessNetworkConnection.getAssetRegistry(NS + '.Commodity');
        const commodity = await commodityRegistry.get('WHEAT');
        expect(commodity.quantity).to.equal(500.0);
        console.log('✓ Commodity quantity verified:', commodity.quantity);
    });

});
