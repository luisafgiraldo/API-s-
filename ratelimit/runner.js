const { execSync } = require('child_process');
const fs = require('fs');

try {
  const output1 = execSync('node ratelimit/ratelimit-testADE-Tier1.js --tier staging --rpm 50 --duration 3', { encoding: 'utf-8' });
  fs.writeFileSync('ADE-Tier1.txt', output1);

  const output2 = execSync('node ratelimit/ratelimit-testADE-Tier2.js --tier staging --rpm 80 --duration 3', { encoding: 'utf-8' });
  fs.writeFileSync('ADE-Tier2.txt', output2);

  const output3 = execSync('node ratelimit/ratelimit-testADE-Tier3.js --tier staging --rpm 100 --duration 3', { encoding: 'utf-8' });
  fs.writeFileSync('ADE-Tier3.txt', output3);
  
} catch (error) {
  console.error('One of the scripts failed:', error);
  process.exit(1);
}
