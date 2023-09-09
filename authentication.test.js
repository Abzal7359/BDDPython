import { Selector } from 'testcafe';

fixture('Getting Started')
    .page('https://dev.deepthought.education/login');

test('My first test', async t => {
    await t
        .typeText('#username', 'Abzal1234')
        .typeText('#password','73597359@Abzal')

        .click('#login')
        
        .expect(Selector('#page-content-wrapper h5').innerText).eql('Welcome to DeepThought');
});

test('My second test with invalid password', async j => {
    await j
        .typeText('#username', 'Abzal1234')
        .typeText('#password','73597359@Abza')

        .click('#login')
        
        .expect(Selector('#login-error-notify').filterVisible().exists).ok();
});

test('My third test with invalid username', async j => {
    await j
        .typeText('#username', 'Abzal123')
        .typeText('#password','73597359@Abzal')

        .click('#login')
        
        .expect(Selector('#login-error-notify').filterVisible().exists).ok();
});