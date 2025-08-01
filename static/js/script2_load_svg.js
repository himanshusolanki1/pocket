
fetch('/themes/cabinet/svg/icons/ai-trading/badge.svg')
  .then(r => r.text())
  .then(svg => {
    document.querySelector('.ai-trading-btn__badge').innerHTML = svg;
  });
