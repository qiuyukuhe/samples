from os import sys, path
sys.path.append(path.abspath('./pricing_service'))

from behave import *
from pricing_service.pricing_calculator import PricingCalculator

@given('Customer specified from "{source}" to "{destination}" with "{pax}"')
def step_impl(context, source, destination, pax):
    context.source = source
    context.destination = destination
    context.pax = pax 

@when('She queries for price')
def step_impl(context):
    calculator = PricingCalculator()
    context.pricing = calculator.Calculate(context.source, context.destination, context.pax)

@then('She expects the pricing to be "{price}"')
def step_impl(context, price):
    assert context.pricing == int(price)