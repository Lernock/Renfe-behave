from behave import *
from selenium import webdriver
import time

@given(u'Lanzar chrome')
def lanzarNavegador(context):
    context.driver=webdriver.Chrome("C:\chromedriver.exe")

@when(u'Abrir pagina renfe')
def abrirRenfe(context):
    context.driver.get("https://www.renfe.com/es/es")

@when(u'Introducir origen "{salida}" y destino "{llegada}"')
def introducirParams(context,salida,llegada):
    context.driver.find_element_by_xpath("//input[@id='origin']").send_keys(salida)
    #context.driver.find_element_by_xpath("// *[ @ id = 'origin']").click()
    context.driver.find_element_by_xpath("// *[ @ id = 'awesomplete_list_1_item_0']").click()
    context.driver.find_element_by_xpath("//input[@id='destination']").send_keys(llegada)
    context.driver.find_element_by_xpath("// *[ @ id = 'destination']").click()
    context.driver.find_element_by_xpath("//*[@id='awesomplete_list_2_item_0']").click()

@when(u'Clickar en comprar')
def comprarBilletes(context):
    context.driver.find_element_by_xpath("//button[@type='submit']").click()


@then(u'Verificar correcto')
def verificar(context):
    precio=context.driver.find_element_by_class("precio booking - list - element - big - font").text()
    assert precio
    context.driver.close()

@step('Wait "{seg}" seconds')
def step_impl(self, seg):
    time.sleep(int(seg))

