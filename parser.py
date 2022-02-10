import sys


filepath = 'input/ems072.txt' 

if len(sys.argv) > 1:
    epno = int(sys.argv[1])
    yturl = str(sys.argv[2])
else:
    sys.exit("usage: python3 parser.py EPISODENUMBER YOUTUBEURL")
print(epno)

#make file for youtube
ytf = open("output/youtubedesc.txt", 'a')
#make file for libsyn
lsf = open("output/libsyndesc.txt" , 'a')
#make file for mailchimp
mcf = open("output/mailchimplist" , 'a')


# function for youtube
def makeYT(lines):
    counter = 1
    while(counter < len(lines)-1):
        text = lines[counter-1]
        link = lines[counter]

        ytf.write(text.strip('\n')+ ': '+link)
        counter+=3

# function for libsyn
def makeLS(lines):
    counter = 1
    while(counter < len(lines)-1):
        text = lines[counter-1]
        link = lines[counter]

        lsf.write('<li><a href="'+str(link)+'">'+str(text)+'</a></li>'+'\n')
        counter+=3



# function for mailchimp
def makeMC(lines, epno, yturl):
    #prepend file with boilerplate
    prepend = ('<h3><span style="color:#000000">Electromaker Show Episode '+ str(epno)+ ' Highlights:</span></h3><ul>')
    mcf.write(prepend)
    
    counter = 1
    for line in lines:
        if counter % 3 == 0:
            #parse mins:seconds into int inseconds for url
            print('ifmod3: {}'.format(line))
            x, y = str(line).split(':')
            mins = int(x)
            secs = int(y)
            inseconds = (mins*60)+secs

            link = '<li><a href="https://www.youtube.com/watch?v={}&amp;t={}s" target="_blank">{}</a></li>'.format(yturl,inseconds,text)
            mcf.write(link)
        else:
            if 'https://' in line:
                
                print('if https: {}'.format(line))
                pass
            else:
                print('if else else: {}'.format(line))
                text = str(line)
    #increment the counter stoopod
        counter+=1

    #add the closing unordered list tag
    mcf.write('</ul>')
# open the input file
with open(filepath, 'r') as f:
    #get lines and start counter
    print('fileopen')
    lines = f.readlines()
    counter = 0
    print('line1: {}, line2: {}'.format(lines[0].strip('\n'),lines[1]).strip('\n'))
    # send each line to a different text maker thing
    makeYT(lines)
    makeLS(lines)
    makeMC(lines,epno,yturl)


ytf.close()
lsf.close()
mcf.close()
