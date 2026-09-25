class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.i = 0
        s = expression

        def parse_expr() -> set[str]:
            result = parse_term()
            while self.i < len(s) and s[self.i] == ',':
                self.i += 1
                result |= parse_term()
            return result

        def parse_term() -> set[str]:
            result = {''}
            while self.i < len(s) and s[self.i] not in ',}':
                factor = parse_factor()
                result = {a + b for a in result for b in factor}
            return result

        def parse_factor() -> set[str]:
            if s[self.i] == '{':
                self.i += 1       
                result = parse_expr()
                self.i += 1      
                return result
            else:
                j = self.i
                while j < len(s) and s[j].islower():
                    j += 1
                word = s[self.i:j]
                self.i = j
                return {word}

        return sorted(parse_expr())