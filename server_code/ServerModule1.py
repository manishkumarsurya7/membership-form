import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def submit(name, weight, address, personal):
  app_tables.gym.add_row(name=name, address=address, weight=weight, personal=personal)
  anvil.email.send(t0="kumargautam8666@gmail.com", subject="Your response from anvil app", 
                   text="Feedback from {name}: weight is {weight} and they live at: {address}. personal training: {personal}")