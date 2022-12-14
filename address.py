#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Dec 6 2022
# This program asks the user for an address
# It then prints the address formatted.


# Function to format the function
def format_address(
    name, question, street_num, street_name, city, province, postal_code, apt_num=None
):
    # Format the strings and put them as uppercase words
    can_post_address = (
        name.upper()
        + "\n"
        + street_num
        + " "
        + street_name.upper()
        + "\n"
        + city.upper()
        + " "
        + province.upper()
        + " "
        + postal_code.upper()
    )

    # Add the apt number if the user lives in one
    # This is optional
    if question == "y":
        can_post_address = (
            name.upper()
            + "\n"
            + apt_num
            + "-"
            + street_num
            + " "
            + street_name.upper()
            + "\n"
            + city.upper()
            + " "
            + province.upper()
            + " "
            + postal_code.upper()
        )
    # Return the formatted address back to the user
    return can_post_address


# Get the users input (their address)
def main():
    # Set default value
    apt_num_user = None

    # Get the information from the user
    user_name = input("Enter your full name: ")
    user_apt = input("Do you live in an apartment? (y/n): ")

    # Check if they live in an apartment
    # If they do, get the number
    if user_apt == "y":
        apt_num_user = input("Enter your apartment number: ")

    # Get the rest of the users address
    street_num_user = input("Enter your street number: ")
    street_name_user = input("Enter your street name and type (Main St.): ")
    user_city = input("Enter your city: ")
    province_user = input("Enter your province (as the first two letters): ")
    postal_user = input("Enter your postal code: ")

    # Assign a variable to the formatted address
    # Get the formatted address from a function
    if apt_num_user is not None:
        user_address = format_address(
            user_name,
            user_apt,
            street_num_user,
            street_name_user,
            user_city,
            province_user,
            postal_user,
            apt_num_user,
        )
    else:
        user_address = format_address(
            user_name,
            user_apt,
            street_num_user,
            street_name_user,
            user_city,
            province_user,
            postal_user,
        )
    # Display the users address
    print("")
    print("Your mailing address is:\n")
    print(user_address)


if __name__ == "__main__":
    main()
