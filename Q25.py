def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
        
        with open(destination_file, 'w') as destination:
            destination.write(content)
        
        print(f"Content from '{source_file}' copied to '{destination_file}' successfully.")
    
    except FileNotFoundError:
        print("One of the specified files was not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = 'source.txt'
destination_file = 'destination.txt'

copy_file(source_file, destination_file)
