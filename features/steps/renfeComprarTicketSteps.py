from behave import *
from selenium import webdriver

@given(u'Lanzar chrome')
def lanzarNavegador(context):
    context.driver=webdriver.Chrome("C:\chromedriver.exe")

@when(u'Abrir pagina renfe')
def abrirRenfe(context):
    context.driver.get("https://www.renfe.com/es/es")

@then(u'Comprar billetes')
def comprarBilletes(context):


@then(u'Cerrar navegador')
def cerrar(context):
    context.driver.close()