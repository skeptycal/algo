// ==UserScript==
// @name        Letter Swapper
// @namespace   reedbeta.com
// @version     1
// @grant       none
// @include     *
// @exclude     https://*.google.com/*
// ==/UserScript==

var swaps =
{
  'a': 'e',  'A': 'E',
  'e': 'a',  'E': 'A',
  'm': 'n',  'M': 'N',
  'n': 'm',  'N': 'M',
  'o': 'u',  'O': 'U',
  'u': 'o',  'U': 'O',
};

// Walk over all text nodes in the document
var walker = document.createTreeWalker(document, NodeFilter.SHOW_TEXT);
while (n = walker.nextNode())
{
  var text = n.nodeValue, newText = "";
  for (c of text)
  {
    if (c in swaps)
      c = swaps[c];
    newText += c;
  }
  n.nodeValue = newText;
}
