#!/usr/bin/env python
# coding: utf-8

# # PYTHON PROJECT

# # Task1: Find out the number of unique dialogue speaker in the sample conversation

# In[1]:


file=open('conv.txt','r')


# In[2]:


#creating a list to store the unique speakers name
list1 = []

#running a loop- reading lines
for line in file.readlines():
    without_new_line=line.strip()
    #split the name which is separated by :
    char=without_new_line.split(":" ,1)
    
    #checking the condition - no names should be repeated
    #condition - Unique Speaker Names.
    if char[0] not in list1: 
        if char[0]=='':
            continue
        else: 
        #appending list to store the names
            list1.append(char[0])
        
#print the names of Unique Speaker       
for element in list1:
    print(element)


# In[3]:


#As told we have to find out the number of unique dialogue speaker
len(list1)


# # Task 2: Create a new text file by the name of the dialogue speaker and store the unique words spoken by that character in the respective text file. Make sure there is only one word every line.

# In[4]:


file=open('conv.txt', 'r')
unique_will = []
#reading every line of the file
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "WILL" in line:
            
            
            #Opening a text file using append function to creates the files 
            #if data does not exist then add the data at the end of the file.
            f = open("WILL.txt", 'a')
            #line = line.lower()
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
        
        #finding unique words said by the speaker 
            for word in words:
                if word not in unique_will:
                    unique_will.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()                    


# In[5]:


words


# In[6]:


file=open('conv.txt', 'r')
unique_waymar = []

#reading every line of the file
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "WAYMAR ROYCE" in line:
            
            
            #Opening a text file using append function to creates the files 
            #if data does not exist then add the data at the end of the file.
            f = open("WAYMAR ROYCE.txt", 'a')
            #line = line.lower()
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker 
            for word in words:
                if word not in unique_waymar:
                    unique_waymar.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[7]:


words


# In[8]:


file=open('conv.txt', 'r')
unique_gared = []

#reading every line of the file
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "GARED" in line:
            
            
            #Opening a text file using append function to creates the files  
            #if data does not exist then add the data at the end of the file.
            f = open("GARED.txt", 'a')
            #line = line.lower()
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_gared:
                    unique_gared.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[9]:


words


# In[10]:


file=open('conv.txt', 'r')
unique_royce = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "ROYCE" in line:
            
            
            #Opening a text file using append function to creates the files 
            #if data does not exist then add the data at the end of the file.
            f = open("ROYCE.txt", 'a')
            #line = line.lower()
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_royce:
                    unique_royce.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[11]:


words


# In[12]:


file=open('conv.txt', 'r')
unique_jon = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "JON" in line:
            
            
            #Opening a text file using append function to creates the files 
            #if data does not exist then add the data at the end of the file
            f = open("JON.txt", 'a')
            #line = line.lower()
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_jon:
                    unique_jon.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[13]:


words


# In[14]:


file=open('conv.txt', 'r')
unique_septa = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "SEPTA MORDANE" in line:
            
            
            #Opening a text file using append function to creates the files 
            #if data does not exist then add the data at the end of the file
            f = open("SEPTA_MORDANE.txt", 'a')
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_septa:
                    unique_septa.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[15]:


words


# In[16]:


file=open('conv.txt', 'r')
unique_sansa = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "SANSA" in line:
            
            
            #Opening a text file using append function to creates the files 
            #if data does not exist then add the data at the end of the file.
            f = open("SANSA.txt", 'a')
            #line = line.lower()
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_sansa:
                    unique_sansa.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()
        


# In[17]:


words


# In[18]:


file=open('conv.txt', 'r')
unique_ned = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "NED" in line:
            
            
            #Opening a text file using append function to creates the files.  
            #if data does not exist then add the data at the end of the file.
            f = open("NED.txt", 'a')
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_ned:
                    unique_ned.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()
            
                        


# In[19]:


words


# In[20]:


file=open('conv.txt', 'r')
unique_robb = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "ROBB" in line:
            
            
            #Opening a text file using append function to creates the files
            #if data does not exist then add the data at the end of the file.
            f = open("ROBB.txt", 'a')
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_robb:
                    unique_robb.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[21]:


words


# In[22]:


file=open('conv.txt', 'r')
unique_cassel = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "CASSEL" in line:
            
            
            #Opening a text file using append function to creates the files
            #if data does not exist then add the data at the end of the file.
            f = open("CASSEL.txt", 'a')
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_cassel:
                    unique_cassel.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[23]:


words


# In[24]:


file=open('conv.txt', 'r')
unique_catelyn = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "CATELYN" in line:
            
            
            #Opening a text file using append function to creates the files
            #if data does not exist then add the data at the end of the file.
            f = open("CATELYN.txt", 'a')
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_catelyn:
                    unique_catelyn.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[25]:


words


# In[26]:


file=open('conv.txt', 'r')
unique_bran = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "BRAN" in line:
            
            
            #Opening a text file using append function to creates the files 
            #if data does not exist then add the data at the end of the file.
            f = open("BRAN.txt", 'a')
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_bran:
                    unique_bran.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[27]:


words


# In[28]:


file=open('conv.txt', 'r')
unique_theon = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "THEON" in line:
            
            
            #Opening a text file using append function to creates the files 
            #if data does not exist then add the data at the end of the file
            f = open("THEON.txt", 'a')
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
           #finding unique words said by the speaker
            for word in words:
                if word not in unique_theon:
                    unique_theon.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[29]:


words


# In[30]:


file=open('conv.txt', 'r')
unique_cersei = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "CERSEI" in line:
            
            
            #Opening a text file using append function to creates the files 
            #if data does not exist then add the data at the end of the file
            f = open("CERSEI.txt", 'a')
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_cersei:
                    unique_cersei.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[31]:


words


# In[32]:


file=open('conv.txt', 'r')
unique_jaime = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "JAIME" in line:
            
            
            #Opening a text file using append function to creates the files. 
            #if data does not exist then add the data at the end of the file.
            f = open("JAIME.txt", 'a')
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_jaime:
                    unique_jaime.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[33]:


words


# In[34]:


file=open('conv.txt', 'r')
unique_robert = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "ROBERT" in line:
            
            #Opening a text file using append function to creates the files. 
            #if data does not exist then add the data at the end of the file.
            f = open("ROBERT.txt", 'a')
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_robert:
                    unique_robert.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[35]:


words


# In[36]:


file=open('conv.txt', 'r')
unique_arya = []

#checking the line actually said by the speaker
for line in file.readlines():
    
        #checking the line actually said by the speaker
        if "ARYA" in line:
            
            
            #Opening a text file using append function to creates the files
            #if data does not exist then add the data at the end of the file.
            f = open("ARYA.txt", 'a')
            words = set(line.split())
            words = [word.strip('.,!;()[]') for word in words]
            words = [word.replace("'s", '') for word in words]
            
            #finding unique words said by the speaker
            for word in words:
                if word not in unique_arya:
                    unique_arya.append(word)
                    f.write(word)
                    f.write('\n')
            f.close()


# In[37]:


words


# In[38]:


#END

