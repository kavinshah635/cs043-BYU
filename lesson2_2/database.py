class Simpledb:
            
        def __init__(self,filename,name,phonenumber):
                self.filename = filename
                self.name = name
                self.phonenumber = phonenumber

        def __repr__(self):
                    return ("<" + self.__class__.__name__ +
                    "\nName = " + str(self.name) +
                    "\nPhonenumber = " + str(self.phonenumber)+
                    "\nFilename = " + str(self.filename) +
                    ">")
        
        
# This is the insert function where they take a name and phonenumber and insert it into the file. It is separated by a tab and they have a new line added to the end of it.
        def insert(self):
                f = open(self.filename, 'a')
                f.write(self.name+ '\t' + self.phonenumber+ '\n')
                f.close()
                return self.name

# This function sees if they have the name entered by the user. It will return the number if applicable.
        def select_one(self):
                f = open(self.filename, 'r')
                
                for row in f:
                        (k, v) = row.split('\t', 1)
                        if k == self.name:
                                self.phonenumber = v
                                return self.phonenumber
                                break

                return "Not Found"
                f.close()
        
# This function looks at the name and sees if it can delete the number and name if applicable.
        def delete(self):
                x = "Not Found!"
                f = open(self.filename, 'r')
                for row in f:
                        (k, v) = row.split('\t', 1)
                        if k == self.name:
                                self.phonenumber = v
                                x = "Found"               
                if x == "Found":   
                        f = open(self.filename, 'r')
                        result = open('result.txt', 'w')
                        for (row) in f:
                                (k, v) = row.split('\t', 1)
                                if k != self.name:
                                        result.write(row)
                                
                        f.close()
                        result.close()
                        import os
                        os.replace('result.txt', self.filename)
                        return self.phonenumber
                else:
                        return x
                              
        
# This function looks at the name and sees if it can updatee the number and keep the name the same if applicable.
        def update(self):
                f = open(self.filename, 'r')
                result = open('result.txt', 'w')
                for (row) in f:
                        (k, v) = row.split('\t', 1)
                        if k == self.name:
                                result.write(self.name + '\t' + self.phonenumber + '\n')
                                self.phonenumber = v
                                #return self.phonenumber
                                
                        else:
                                result.write(row)
                f.close()
                result.close()
                import os
                os.replace('result.txt', self.filename)
                return self.phonenumber
                
        

