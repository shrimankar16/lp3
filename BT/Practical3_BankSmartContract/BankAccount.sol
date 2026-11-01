// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Smart contract simulating a simple bank account
// Deployed on: Sepolia Test Network via Remix IDE
// Operations: Deposit, Withdraw, Show Balance

contract BankAccount {

    // ── State Variables ───────────────────────────────────
    // 'owner' stores the address of the account holder
    // Set once at deployment and cannot be changed
    address public owner;

    // 'balance' stores the total ETH (in wei) held by this contract
    // 1 ETH = 10^18 wei
    uint256 private balance;

    // ── Events ────────────────────────────────────────────
    // Events are logs stored on the blockchain
    // Useful for tracking deposits and withdrawals off-chain

    // Emitted whenever ETH is deposited
    event Deposited(address indexed sender, uint256 amount);

    // Emitted whenever ETH is withdrawn
    event Withdrawn(address indexed owner, uint256 amount);

    // ── Modifier ──────────────────────────────────────────
    // Restricts certain functions to the owner only
    // If the caller is not the owner, transaction reverts with an error message
    modifier onlyOwner() {
        require(msg.sender == owner, "Access denied: You are not the account owner");
        _;
    }

    // ── Constructor ───────────────────────────────────────
    // Runs once when the contract is deployed
    // Sets the deployer's address as the owner
    constructor() {
        owner = msg.sender;
        balance = 0;
    }

    // ── Function 1: Deposit ───────────────────────────────
    // Allows the owner to deposit ETH into the account
    // 'payable' keyword means this function can receive ETH
    // msg.value = amount of ETH sent with the transaction (in wei)
    function deposit() public payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than 0");

        // Add the sent ETH to the balance
        balance += msg.value;

        // Emit event to log the deposit
        emit Deposited(msg.sender, msg.value);
    }

    // ── Function 2: Withdraw ──────────────────────────────
    // Allows the owner to withdraw a specified amount of ETH
    // 'amount' is in wei
    function withdraw(uint256 amount) public onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(amount <= balance, "Insufficient balance");

        // Deduct the amount before transferring (prevents re-entrancy attacks)
        balance -= amount;

        // Transfer ETH back to the owner's wallet
        // payable(owner) converts address to a payable address
        payable(owner).transfer(amount);

        // Emit event to log the withdrawal
        emit Withdrawn(msg.sender, amount);
    }

    // ── Function 3: Show Balance ──────────────────────────
    // Returns the current balance stored in the contract
    // 'view' means it only reads state, does not modify it
    // 'view' functions do NOT cost gas when called externally
    function getBalance() public view onlyOwner returns (uint256) {
        return balance;
    }

    // ── Fallback Function ─────────────────────────────────
    // Called if ETH is sent directly to the contract address
    // without calling deposit() — just adds it to balance
    receive() external payable {
        balance += msg.value;
        emit Deposited(msg.sender, msg.value);
    }
}
