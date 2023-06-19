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
<li>Adding items to a new invoices corresponding to a clients</li> 
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

 ## API Endpoints
 Following are the api endpoints for this app.
 

<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>URL</th>
    <th>Description</th>
  </tr>
 <tr>
    <td>SIGNUP</td>
    <td>/signup</td>
    <td>Signing up using username, password, email</td>
  </tr>
  <tr>
    <td>LOGIN</td>
    <td>/login </td>
    <td>Logging in using username, password</td>
  </tr>
 <tr>
    <td>CLIENTS</td>
    <td>/dashboard/clients</td>
    <td>Display information about clients</td>
  </tr>
   <tr>
    <td>ADD CLIENTS</td>
    <td>/dashboard/add</td>
    <td>Allows user to add client</td>
  </tr>
    <tr>
    <td>VIEW CLIENT</td>
    <td>/dashboard/clients/pk</td>
    <td>To view details of client</td>
  </tr>
 </tr>
    <tr>
    <td>EDIT CLIENT</td>
    <td>/dashboard/clients/pk/edit</td>
    <td>To edit information about client</td>
  </tr>
    <tr>
    <td>INVOICES</td>
    <td>/dashboard/invoices</td>
    <td>List all the invoices</td>
  </tr>
    <tr>
    <td>INVOICE DETAILS </td>
    <td>/dashboard/invoices/pk</td>
    <td>List invoice items, client detail</td>
  </tr>
    </tr>
    <tr>
    <td>DOWNLOAD INVOICE </td>
    <td>/dashboard/invoices/pk/generate_pdf/</td>
    <td>Downloads invoices</td>
  </tr>
  </tr>
    </tr>
    <tr>
    <td>ADD INVOICE</td>
    <td>/dashboard/invoices/add</td>
    <td>Add invoice with multiple items corresponding to a client</td>
  </tr>
</table>


This project is inspired by the [this video](https://www.youtube.com/watch?v=WMR4qdYFW-8) by [code with stein](https://github.com/SteinOveHelset)


