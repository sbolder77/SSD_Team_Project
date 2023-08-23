import users
import roles
import orders
import logging

#region objects
u = users.UserDetails()
r = roles.RoleDetails()
o = orders.OrderDetails()
l = logging.LoggingDetails()
#endregion

def create_user():
    return u.get_user

def edit_user():
    return u.get_user

def authorise_user():
    return u.get_user

def delete_user():
    return u.get_user

def place_order():
    return u.get_user

def edit_order():
    return u.get_user

def cancel_order():
    return u.get_user
