from datetime import datetime
import uuid
def create_transaction(amount,transaction_type,category,date,note):
    
    
    if not isinstance (amount,(float,int)) or amount<=0:
        raise ValueError("AMOUNT MUST BE POSITIVE OR IN INTEGER OR FLOATING FORM")
    
    if transaction_type not in ('EXPENSE','INCOME'):
        raise ValueError("TRANSACTION TYPE MUST BE INCOME OR EXPENSE")
    
    if not isinstance(category,(str)) or not  category.strip():
        raise ValueError("CATEGORY MUST BE A NON EMPTY STRING")
    

    try:
        datetime.strptime(date,'%Y-%m-%d')

    except ValueError:
        raise ValueError("DATE MUST BE IN THIS FORMAT YYYY-MM-DD")
    
    if not isinstance(note,str):
        raise ValueError("NOTE MUST BE A STRING")
    

    transaction_id = str(uuid.uuid4())[:8] 
    transaction={"TRANSACTION_ID":transaction_id,
                 "Amount":amount,
                  "type":transaction_type,
                  "category":category.strip(),
                  "date":date,
                  "note":note.strip()
                  }
    return transaction