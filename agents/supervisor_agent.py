def route(q:str):
 q=q.lower()
 return "writer" if any(x in q for x in ["book","cancel","reschedule"]) else "reader"
