# DEFENSE: We use a config file to keep database credentials in one place. 
# This makes it easy to change the password without searching through all the code.

def load_config():
    return {
        "host": "localhost",
        "database": "postgres", # Change to your DB name
        "user": "postgres",
        "password": "kasym147208a11.."       # Change to your DB password
    }