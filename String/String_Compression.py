class Solution:
  def compress(self, chars: List[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[ans] = letter
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans


class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        previous = ""
        c = 1
        if len(chars) == 1:
            return 1
        for i, ch in enumerate(chars):
            if ch == previous:
                c += 1
            else:
                s = s + previous
                if c != 1:
                    s = s + str(c)
                    c = 1
            previous = ch
        if c > 1:
            s = s + previous + str(c)
        else:
            s = s + previous
        chars[:len(s)] = list(s)
        print(s)
        return len(s)
