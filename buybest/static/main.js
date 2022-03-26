if (localStorage.getItem("cart") == null) {
    var cart = {};
} else {
    cart = {};
    cart = JSON.parse(localStorage.getItem("cart"));
    add_remove_cart(cart);
}

$(".itemprod").on("click", "button.cart", function () {
    var idstr = this.id.toString();
    if (cart[idstr] != undefined) {
        qty = cart[idstr][0] + 1;

    } else {
        qty = 1;
        var name = document.getElementById('name' + idstr).innerHTML;
        var price = document.getElementById('price' + idstr).innerHTML;
        cart[idstr] = [qty, name, price];
    }
    add_remove_cart(cart);
});

$("#popcart").popover();

function updatepopover(cart) {
    var popstr = "";
    popstr = popstr + "<div class='container'><h5 class='navbar navbar-dark bg-dark text-white'><b>Your Buy Best Cart</b></h5><div>";
    var i = 1;
    for (var item in cart) {
        if (cart[item][0] == 0) {
            continue;
        }
        popstr = popstr + "<b>" + i + ": </b>";
        popstr = popstr +
            document.getElementById("name" + item).innerHTML.slice(0, 19) + "... Qty: " + cart[item][0] + '<hr style="margin-top: 0rem;margin-bottom: 0rem;border-top:1px dashed black;"><br>';
        i = i + 1;
    }
    popstr = popstr + '</div><a href="/checkout/"> <button id="checkout" class="btn btn-outline-success bg-dark">Check Out</button></a><button id="clearcart" class="btn btn-outline-success bg-dark" onclick="clearcart()">Clear Cart</button></div>';
    document.getElementById("popcart").setAttribute("data-content", popstr);
}

//clearing the cart
function clearcart() {
    var cart = JSON.parse(localStorage.getItem("cart"));
    for (var item in cart) {
        document.getElementById("item" + item).innerHTML = "<button id='" + item + "' class='btn btn-outline-success bg-dark cart'>Add to Cart</button>";
    }
    localStorage.clear();
    var cart = {};
    add_remove_cart(cart);
}

//updating the cart
function add_remove_cart(cart) {
    var sum = 0;
    for (var item in cart) {
        sum += cart[item][0];
        document.getElementById("item" + item).innerHTML = "<button id='remove" + item + "'class='btn btn-outline-success bg-dark remove' >-</button><span id='value" + item + "'>" + cart[item][0] + "</span> <button id='add" + item + "'class='btn btn-outline-success bg-dark add'>+</button>";
    }
    localStorage.setItem("cart", JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
    updatepopover(cart);
    //$("#popcart").popover("show");
}

$(".itemprod").on("click", "button.remove", function () {
    a = this.id.slice(10);
    cart["prod" + a][0] = cart["prod" + a][0] - 1;
    cart["prod" + a][0] = Math.max(0, cart["prod" + a][0]);
    document.getElementById("valueprod" + a).innerHTML = cart["prod" + a][0];
    add_remove_cart(cart);
});

$(".itemprod").on("click", "button.add", function () {
    a = this.id.slice(7);
    cart["prod" + a][0] = cart["prod" + a][0] + 1;
    document.getElementById("valueprod" + a).innerHTML = cart["prod" + a][0];
    add_remove_cart(cart);
});