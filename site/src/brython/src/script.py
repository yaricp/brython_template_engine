def render(file,temp,target, count):
    global  file_data, template, target_id , count_view, rowscharsplit, colscharsplit 
    file_data = file
    rowscharsplit = '\\n'
    colscharsplit = ';'
    template = temp
    target_id = target
    count_view = count
    open_template()

def open_template():
    req = ajax()
    req.on_complete = on_complete_tmp
    req.set_timeout(5,'connection time out')
    req.open('GET',template,False)
    req.send()
   
def on_complete_tmp(req):
    doc[target_id ].html= req.text
    if req.status==200 or req.status==0:
       load_data()
    else:
        doc[target_id].html = req.text
def load_data():
    req = ajax()
    req.on_complete = on_complete_data
    req.set_timeout(5,'connection time out')
    req.open('GET',file_data,False)
    req.send()
    
def on_complete_data(req):
    rows= req.text.split(rowscharsplit)
    keys=rows[0].split(colscharsplit)
    text=''
    text_template = doc[target_id ].html
    #alert(text_template)
    if req.status==200 or req.status==0:
        if count_view:
            list_row= rows[1:count_view+1]
        else:
            list_row= rows[1:]
        for r in list_row:
            cols = r.split(colscharsplit)
            if len(cols)>1 and cols!='':
                index=0
                t_tmp= text_template
                for c in cols: 
                    t_tmp=replacetext(t_tmp, keys[index], c)
                    index+=1
                text+=t_tmp
        doc[target_id ].html = text
    else:
        doc[target_id ].html = req.text
        
def replacetext(text, from_t, to_t):
    out=text.replace(from_t, to_t)
    return out
