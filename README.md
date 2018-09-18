### ID dispenser.

The IDs are numbers between 10000 and 99999.
The used IDs are specified in a white space delimeted file, see _used_ids.txt_ for an example.

The following command will print 3 new IDs to standard output.
```
python idDispenser.py --used_ids used_ids.txt --number_of_ids 3
```

If you would like to append the newly issued IDs to the file contaning the used IDs, do
```
python idDispenser.py --used_ids used_ids.txt --number_of_ids 3 --update_used_ids
```
