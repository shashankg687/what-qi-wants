const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();

    const speakers = [
        { name: 'sourav_tcs', poster: 'website/speakers/poster_sourav_tcs.html', output: 'confirmed_speaker/poster_sourav_tcs.png' },
        { name: 'reena_qetci', poster: 'website/speakers/poster_reena_qetci.html', output: 'confirmed_speaker/poster_reena_qetci.png' },
        { name: 'kazuya_lquom', poster: 'website/speakers/poster_kazuya_lquom.html', output: 'confirmed_speaker/poster_kazuya_lquom.png' },
    ];

    for (const speaker of speakers) {
        const url = 'file://' + path.resolve(__dirname, speaker.poster);
        await page.goto(url, { waitUntil: 'networkidle0' });
        await page.setViewport({ width: 1080, height: 1080, deviceScaleFactor: 2 });
        await page.emulateMediaType('screen');
        await page.screenshot({ path: path.resolve(__dirname, speaker.output), fullPage: true });
        console.log(`Captured ${speaker.output}`);
    }

    await browser.close();
})();
