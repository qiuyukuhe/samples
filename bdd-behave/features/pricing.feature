Feature: Test pricing
	Customer provides details and the system returns a pricing. 
	To test that we have verified the following scenarios:
	
	Scenario Outline: Test pricing for source, destination, pax
		Given Customer specified from "<source>" to "<destination>" with "<pax>"
		When She queries for price
		Then She expects the pricing to be "<price>"

	Examples:
		| source	| destination	| pax	| price	|
		| Bergen	| Oslo			| 10	| 200	|
		| Oslo		| Bergen		| 5		| 100	|
