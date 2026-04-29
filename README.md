# Atelier 3 : Mise en place d’un système d’authentification Django

## Auteur

Projet réalisé par **Fatima Zahra KAKA** dans le cadre d’un atelier Django – EMI Rabat

---

## Description de l’atelier

Cet atelier consiste à ajouter un système d’authentification dans une application Django existante (projet e-commerce).

Il permet de gérer les utilisateurs avec deux profils :

* Administrateur  
* Utilisateur normal  

---

## Fonctionnalités réalisées

* Inscription utilisateur  
* Connexion / Déconnexion  
* Gestion des sessions  
* Page profil protégée  
* Séparation des rôles (Admin / User)  
* Protection des pages avec `@login_required`

---

## Fonctionnement général

* L’administrateur peut gérer les produits (liste, modification, profil)  
* L’utilisateur peut consulter les produits et utiliser le panier  
* Certaines pages sont accessibles uniquement après authentification  

---

## Captures d’écran

---

### Authentification (avant connexion)

#### Page de connexion

![Login](screenshots/avant_connexion/connexion.png)

#### Liste des produits (utilisateur non connecté)

![Guest Product List](screenshots/avant_connexion/list_produit_sans_connexion.png)

---

### Interface utilisateur

#### Profil utilisateur

![User Profile](screenshots/user/profile_user_KAKA.png)

#### Détail produit

![Product Detail](screenshots/user/detail_produit_user.png)

#### Panier vide

![Empty Cart](screenshots/user/panier_user_KAKA_vide.png)

#### Panier avec produits

![Cart](screenshots/user/panier_user_KAKA.png)

---

### Interface administrateur

#### Profil admin

![Admin Profile](screenshots/admin/profile_admin.png)

#### Liste des produits

![Product List Admin](screenshots/admin/list_produit_admin.png)

#### Modifier produit

![Edit Product](screenshots/admin/modifier_produit_admin.png)

---

## Structure du projet

* `accounts/` → gestion des utilisateurs  
* `products/` → gestion des produits  
* `templates/` → interfaces HTML  
* `screenshots/` → captures d’écran du projet  

---

## Lancement du projet

```bash
python manage.py migrate
python manage.py runserver

Accès :
http://127.0.0.1:8000/

---

