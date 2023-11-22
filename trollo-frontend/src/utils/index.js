export const generateUniqueAlphabet = () => {
  const alphabet = "abcdefghijklmnopqrstuvwxyz1234567890";
  const uniqueAlphabets = [];
  while (uniqueAlphabets.length < 14) {
    const randomIndex = Math.floor(Math.random() * alphabet.length);
    const randomChar = alphabet[randomIndex];
    if (!uniqueAlphabets.includes(randomChar)) {
      uniqueAlphabets.push(randomChar);
    }
  }
  return uniqueAlphabets.join("");
};
