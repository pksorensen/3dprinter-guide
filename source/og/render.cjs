const {chromium}=require(process.env.PW||'playwright-core');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});
await p.goto('file://'+__dirname+'/og.html');await p.waitForTimeout(1500);await p.screenshot({path:__dirname+'/../../site/og.png'});await b.close()})();
