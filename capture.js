
const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();

    // 1. Capture Poster
    const posterUrl = 'file://' + path.resolve('poster.html');
    await page.goto(posterUrl, { waitUntil: 'networkidle0' });
    await page.setViewport({ width: 1080, height: 1080, deviceScaleFactor: 2 });
    // Allow resizing
    await page.emulateMediaType('screen');
    await page.screenshot({ path: 'poster.png', fullPage: true });
    console.log('Captured poster.png');

    // 2. Capture Speakers
    const speakersUrl = 'file://' + path.resolve('speakers.html');
    await page.goto(speakersUrl, { waitUntil: 'networkidle0' });
    await page.setViewport({ width: 1080, height: 1080, deviceScaleFactor: 2 });
    await page.emulateMediaType('screen');
    await page.screenshot({ path: 'speakers.png', fullPage: true });
    console.log('Captured speakers.png');

    await browser.close();
})();
