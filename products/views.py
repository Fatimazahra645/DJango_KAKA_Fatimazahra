from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.contrib.auth.decorators import login_required


# =========================
# PRODUITS
# =========================

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})


# =========================
# CATÉGORIES
# =========================

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)

    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products
    })


# =========================
# PANIER (SESSION SIMPLE)
# =========================

@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    # récupérer panier ou créer vide
    cart = request.session.get('cart')

    if cart is None:
        cart = {}

    product_id = str(id)

    # ajout ou incrément
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    # sauvegarde
    request.session['cart'] = cart
    request.session.modified = True

    # 🔥 DEBUG (tu peux supprimer après test)
    print("PANIER ACTUEL :", request.session['cart'])

    return redirect('cart')


@login_required
def cart(request):
    cart = request.session.get('cart', {})

    products = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))

            product.quantity = quantity
            product.subtotal = product.price * quantity

            total += product.subtotal
            products.append(product)

        except Product.DoesNotExist:
            continue

    return render(request, 'products/cart.html', {
        'products': products,
        'total': total
    })


@login_required
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    product_id = str(id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')