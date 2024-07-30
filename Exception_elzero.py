the_file=None
the_tries=5
# def naem(n) ->str:
#     print(f"Hollo{n}")
while the_tries>0:
    try:
        print("Enter the file name with absolute path to open")
        print(f"YouHave {the_tries} Tries Left")
        print("Example: D:/python/files/youfile.txt")
        file_name_path=input("file name: ").strip() 
        the_file=open(file_name_path ,"r") 
        print(the_file.read())
        break
    except FileNotFoundError:
        print("File not found please besure the nat vald")
        the_tries-=1
    except:
        print("Error Happen")
    finally:
        if the_file is not None:
            the_file.close()
            print("The file close")
else:
    print("All Tries Is Done")