import pandas as pd
import matplotlib.pyplot as plt

# Initialize an empty DataFrame or load from existing CSV if available
try:
    inventory_df = pd.read_csv('Stock.csv', index_col=0)
except FileNotFoundError:
    inventory_df = pd.DataFrame(columns=['Item Name', 'Stock', 'Price'])

# Function to display the menu
def display_menu():
    print("\nWelcome to Inventory Management System")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Delete Item")
    print("4. Visualize Inventory")
    print("5. Exit")

# Function to view current inventory
def view_inventory():
    print("\nCurrent Inventory:")
    print(inventory_df)

# Function to add a new item
def add_item():
    item_id = input("\nEnter Item ID: ")
    item_name = input("Enter Item Name: ")
    stock = int(input("Enter Stock Quantity: "))
    price = float(input("Enter Price per Item: "))
    
    inventory_df.loc[item_id] = [item_name, stock, price]
    inventory_df.to_csv('Stock.csv')  # Save inventory to CSV after adding
    print(f"\nItem '{item_name}' added successfully.")

# Function to delete an item
def delete_item():
    item_id = input("\nEnter Item ID to delete: ")
    if item_id in inventory_df.index:
        item_name = inventory_df.loc[item_id, 'Item Name']
        inventory_df.drop(item_id, inplace=True)
        inventory_df.to_csv('Stock.csv')  # Save inventory to CSV after deleting
        print(f"\nItem '{item_name}' deleted successfully.")
    else:
        print("\nItem ID not found.")

# Function to visualize inventory
def visualize_inventory():
    if inventory_df.empty:
        print("\nInventory is empty. Add items to visualize.")
        return
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(inventory_df['Item Name'], inventory_df['Stock'], color='skyblue')
    plt.xlabel('Item Name')
    plt.ylabel('Stock Quantity')
    plt.title('Inventory Stock Quantity')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Main program loop
while True:
    display_menu()
    choice = input("\nEnter your choice: ")

    if choice == '1':
        view_inventory()
    elif choice == '2':
        add_item()
    elif choice == '3':
        delete_item()
    elif choice == '4':
        visualize_inventory()
    elif choice == '5':
        print("\nThank you for using the Inventory Management System.")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 to 5.")
