'use strict';

/**
 * Transaction Logic File — Hyperledger Composer
 * Contains the JavaScript functions that execute when
 * transactions are submitted to the business network.
 */

/**
 * Track the trade of a commodity from one trader to another.
 *
 * @param {org.example.trading.Trade} trade - The trade transaction instance
 * @transaction
 *
 * How it works:
 * 1. The transaction receives a reference to the Commodity and the new owner (Trader).
 * 2. We update the commodity's 'owner' field to point to the new trader.
 * 3. We save the updated asset back to the ledger (asset registry).
 * 4. We emit a TradeNotification event so external apps are notified.
 */
async function tradeCommodity(trade) {

    // Step 1: Emit a TradeNotification event before making changes
    // getFactory() creates new instances of model resources
    let factory = getFactory();

    // Create a new event of type 'TradeNotification' in the trading namespace
    let tradeNotification = factory.newEvent(
        'org.example.trading',   // namespace
        'TradeNotification'      // event name
    );

    // Set the commodity field of the event to the commodity being traded
    tradeNotification.commodity = trade.commodity;

    // Emit the event — subscribers will receive this notification
    emit(tradeNotification);

    // Step 2: Update the ownership of the commodity
    // Change the 'owner' relationship to point to the new trader
    trade.commodity.owner = trade.newOwner;

    // Step 3: Get the asset registry for Commodity assets
    // The asset registry is the ledger storage for a specific asset type
    let assetRegistry = await getAssetRegistry('org.example.trading.Commodity');

    // Step 4: Save the updated commodity back to the ledger
    // update() persists the changes to the blockchain
    await assetRegistry.update(trade.commodity);
}
