# Exception Handling

try:
    f = open('users.txt')
    # users = names

except FileNotFoundError as e:
    print(e)
    
except Exception as e:
    print(e)
    
else:
    print(f.read())
    f.close()
    
finally:
    print("Script has been run successfully!")