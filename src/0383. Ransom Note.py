class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        if len(magazine_counter) < len(ransom_note_counter):
            return False

        else:
            return all([ransom_note_counter[letter] <= magazine_counter.get(letter, 0) for letter in ransom_note_counter])