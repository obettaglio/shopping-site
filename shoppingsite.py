"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken, Katie Byers.
"""


from flask import Flask, render_template, redirect, flash, request, session
import jinja2

import melons


app = Flask(__name__)

# A secret key is needed to use Flask sessioning features

app.secret_key = 'ohigoawiehrwsagdfklsjgawe;irj;gsi'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined

# melon_prices = {}

# melon_list = melons.get_all()
# for melon in melon_list:
#     melon_prices[melon.melon_id] = melon.price


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melon_list = melons.get_all()
    # melon_id = melon_list.melon_id
    # melon_price = melons.melon_price
    # melon_image_url = melons.melon_image_url
    # melon_name = melons.melon.common_name
    return render_template("all_melons.html",
                           melon_list=melon_list)
                            # melon_id=melon_id,
                            # melon_price=melon_price,
                            # melon_image_url=melon_image_url,
                            # melon_name=melon_name)


@app.route("/melon/<melon_id>")
def show_melon(melon_id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """

    melon = melons.get_by_id(melon_id)
    print melon
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart")
def show_shopping_cart():
    """Display content of shopping cart."""

    # TODO: Display the contents of the shopping cart.

    # The logic here will be something like:
    #
    # - get the cart dictionary from the session
    # - create a list to hold melon objects and a variable to hold the total
    #   cost of the order
    # - loop over the cart dictionary, and for each melon id:
    #    - get the corresponding Melon object
    #    - compute the total cost for that type of melon
    #    - add this to the order total
    #    - add quantity and total cost as attributes on the Meotal cost as lon object
    #    - add the Melon object to the list created above
    # - pass the total order cost and the list of Melon objects to the template
    #
    # Make sure your function can also handle the case wherein no cart has
    # been added to the session

    cart = session.get("cart")
    melon_orders = []
    total = 0
    if cart:
        total = 0
        # keys = cart.keys()
        for melon_id in cart:
            new_melon = melons.get_by_id(melon_id)
            # new_melon.melon_id = melon_id
            new_melon.melon_qty = cart[melon_id]
            # new_melon.price = melon_prices[melon_id]
            new_melon.total = "%.2f" % (new_melon.melon_qty * new_melon.price)
            # new_melon.price = new_melon.price_str()
            melon_orders.append(new_melon)
            total += float(new_melon.total)
    return render_template("cart.html", melon_orders=melon_orders, total_price="%.2f" % total)


@app.route("/add_to_cart/<melon_id>")
def add_to_cart(melon_id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Melon successfully added to
    cart'."""

    # TODO: Finish shopping cart functionality

    # The logic here should be something like:
    #
    # - check if a "cart" exists in the session, and create one (an empty
    #   dictionary keyed to the string "cart") if not
    # - check if the desired melon id is the cart, and if not, put it in
    # - increment the count for that melon id by 1
    # - flash a success message
    # - redirect the user to the cart page

    cart_exist = session.get("cart")

    if cart_exist:
        if cart_exist.get(melon_id):
            cart_exist[melon_id] += 1
        else:
            cart_exist[melon_id] = 1
    else:

        session["cart"] = {}
        cart_exist = session["cart"]
        cart_exist[melon_id] = 1

    flash("Added: " + melons.get_by_id(melon_id).common_name)  # % (melons.get_by_id(melon_id))

    return redirect("/cart")


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    # TODO: Need to implement this!

    # The logic here should be something like:
    #
    # - get user-provided name and password from request.form
    # - use customers.get_by_email() to retrieve corresponding Customer
    #   object (if any)
    # - if a Customer with that email was found, check the provided password
    #   against the stored one
    # - if they match, store the user's email in the session, flash a success
    #   message and redirect the user to the "/melons" route
    # - if they don't, flash a failure message and redirect back to "/login"
    # - do the same if a Customer with that email doesn't exist

    return "Oops! This needs to be implemented"


@app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True)
