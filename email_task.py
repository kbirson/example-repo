"""
Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    # Initialise the instance variables for each email.
    # adding class variables for email_address, subject_line, email_content, default has_been_read to false
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  


# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.
    def mark_as_read(self):
        self.has_been_read = True
        print(f"Email from {self.email_address} marked as read.")

# --- Functions --- #
# Build out the required functions for your program.
    def populate_inbox():
        # Create 3 sample emails and add them to the inbox list.
        example = Email("steve@example.com", "Welcome!", "Hello, welcome to our service!")
        inbox.append(example)
        football = Email("dabrickashaw@nfl.com", "Game Day!", "Remember to stretch!")
        inbox.append(football)
        joker = Email("seymourbutts@joke.com", "Funny Joke", "Did you see more?")    
        inbox.append(joker)
        #pass #commenting out pass to avoid syntax error

    def list_emails():
        # Create a function that prints each email's subject line
        # alongside its corresponding index number,
        # regardless of whether the email has been read.
        for index, email in enumerate(inbox):
            print(f"{index}: {email.subject_line} (Read: {email.has_been_read})")
        #pass

    def read_email(index):
        # Create a function that displays the email_address, subject_line,
        # and email_content attributes for the selected email.
        # After displaying these details, use the 'mark_as_read()' method
        # to set its 'has_been_read' instance variable to True.
        print(f"Email from: {inbox[index].email_address}")
        print(f"Subject: {inbox[index].subject_line}")
        print(f"Content: {inbox[index].email_content}")
        inbox[index].mark_as_read()
        
        #pass

    def view_unread_emails():
        # Create a function that displays all unread Email object subject lines
        # along with their corresponding index numbers.
        # The list of displayed emails should update as emails are read.
        # This function will use the has_been_read instance variable to determine what is unread.
        for email in inbox:
            print("Checking inbox for unread emails...")
            if email.has_been_read == False:
                print(f"{inbox.index(email)}: {email.subject_line} - status: Unread")
            else:
                print("No unread emails.")
                break

# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
inbox = []

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
Email.populate_inbox() # This adds the sample emails to the inbox list.

# Fill in the logic for the various menu operations.
if len(inbox) == 0:
    # Call the function to list all emails in the inbox. 
    print("No emails in the inbox. Please populate the inbox first.")

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Add logic here to read an email
        Email.read_email(int(input("Enter the index of the email you want to read: ")))
        if len(inbox) == 0:
            print("No emails to read.")
            continue
        pass

    elif user_choice == 2:
        # Add logic here to view unread emails
        Email.view_unread_emails()
        if len(inbox) == 0:
            print("No unread emails.")
            continue
        pass

    elif user_choice == 3:
        # Add logic here to quit application.
        print("Quitting application. Goodbye!")
        break
        pass

    else:
        print("Oops - incorrect input.")
