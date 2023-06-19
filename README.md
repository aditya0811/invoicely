# Invoicely
This application is part of an Invoicing Web Application. For each user, we have multiple clients, having multiple invoices, which have various items. 


## Tech Stack
### Frontend
<p align="left">
 <img alt="Vue.js" src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D"/> 
 <img alt="Bulma" src="https://img.shields.io/badge/-Bulma-FFFFFF?style=for-the-badge&logo=bulma"/> 
</p>


### Backend
<p align="left">
 <img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> 
  <img alt="Django" src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/> 
</p>


## Invoicing Web Application
Built an Invoicing Web Application with the following features

<ol>
<li>Login/Sign-up</li> 
<li>Adding Clients</li> 
<li>Adding Invoices corresponding o clients</li> 
<li>Displaying the list of items for an invoice</li>  
<li>Pay button for the invoices</li> 
<li>Downloading invoice as pdf (using wkhtmltopdf)</li> 
</ol>

## Getting started 


### Libraries Required
Use below code to install python related dependencies
```
cd invoicely
pip install -r requirements.txt
```
Use below code to install Javascript-related dependencies. This is frontend project : https://github.com/aditya0811/InvoicelyWebApp
```
npm install bulma
```


## Starting app 
### Backend 
 ```
 cd invoicely
 python manage.py runserver
 ```
 ### Frontend 
 ```
 cd invoicely_vue
 npm run serve
 ```


This project is inspired from following video by [code with stein](https://github.com/SteinOveHelset)https://github.com/SteinOveHelset
https://www.youtube.com/watch?v=WMR4qdYFW-8
