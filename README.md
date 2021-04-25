# Sql_testing Using Metamorphic Testing

Using Metamorphic Testing to test if sql_injection exist in sql query process

## Structure

```bash
--FYP_SQL_testing
	--testing.py
	--src
		--app.py
	--test
		--testcase.py
```

## Explanation

app.py implements sql_query (to the database have been deployed on my local machine)<br />
testcase.py includes testcases that generated from inputs according to a specific MR<br />
testing.py checks if MR holds using its co-responding testcase, and then generate a report of results.<br />


## Usage

You need to connect to your own database following app.py

```bash
python3 testing.py
```

## Sample output

For convience, I use one input "Dave".<br />
Then testcase.py will generated one testcase.<br />
Finally, In testing.py, MR will be tested based on testcases.<br />


```bash
test_MR1 (__main__.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.025s

OK
YuandeMacBook-Pro:sql_testing yuan$ 
```
