
import re

class DeIdentifier:

    def mask(self,text):

        patterns=[
            r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+',
            r'\d{3}-\d{3}-\d{4}',
            r'MRN-\d+'
        ]

        for p in patterns:
            text=re.sub(p,'[REDACTED]',text)

        return text
