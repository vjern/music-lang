from typing import List


class Track:
    steps: List[str]


def parse(text: str):
    
    rows = text.split('\n')

    for row in rows:

        if not row.strip():
            continue

        if row.strip().startswith('//'):
            continue
        
        
        

            