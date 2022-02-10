import sys

# TODO implement the Youtube times

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
    for line in lines:
        if counter % 2 != 0:
            ytf.write(line.strip('\n')+ ': ')
            print('if: counter is: {}, adding {} to file'.format(str(counter),str(line)))
        else:
            ytf.write(line)
            print('else: counter is: {}, adding {} to file'.format(str(counter),str(line)))
        counter+=1 

# function for libsyn
def makeLS(lines):
    counter = 1
    text = ''
    link = ''
    for line in lines:
        if counter % 2 == 0:
            
            link = line.strip('\n')
            print('libsyn link = {}'.format(str(link)))
            lsf.write('<li><a href="'+str(link)+'">'+str(text)+'</a></li>'+'\n')
        else:
            text = line.strip('\n')
            print('libsyn text = {}'.format(str(text)))
        counter+=1 


# function for mailchimp
def makeMC(lines, epno, yturl):
    #prepend file with boilerplate
    prepend = ('<h3><span style="color:#000000">Electromaker Show Episode '+ str(epno)+ ' Highlights:</span></h3><ul>')
    mcf.write(prepend)
    
    counter = 1
    for line in lines:
        if counter % 3 == 0:
            #parse mins:seconds into int inseconds for url
            x, y = str(line).split(':')
            mins = int(x)
            secs = int(y)
            inseconds = (mins*60)+secs

            link = '<li><a href="https://www.youtube.com/watch?v={}&amp;t={}s" target="_blank">{}</a></li>'.format(yturl,inseconds,text)
            mcf.write(link)
        else:
            if 'https://' in line:
                continue
            else:
                text = str(line)

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
