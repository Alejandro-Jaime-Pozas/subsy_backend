1. frontend client requests a **link token** to backend python
2. backend python requests a **link token** to plaid
3. plaid sends **link token** to backend python
4. backend python sends **link token** to frontend client
5. frontend client posts **link token** to plaid, which plaid should validate to start Link
6. user signs in through plaid's Link client (their proprietary frontend login client app)
7. plaid sends back a short-lived **public token** to frontend client (lasts 30mins)
8. as soon as frontend client receives the **public token**, it sends it to backend python
9. backend python sends the **public token** to plaid
10. plaid validates **public token**, and sends an access token to backend python
11. access token is stored securely in backend python
