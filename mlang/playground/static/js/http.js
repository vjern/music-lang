const Http = {

    /**
     * @param {string} url
     */
    GET: function GET(url, headers) {
      // Basic GET request in CORS mode;
      // console.(`GET ${url}`);
      return fetch(
        url,
        {
          mode: 'cors',
          headers: headers
        },
      );
    },
  
    /**
     * @param {string} url
     * @param {Object} body
     */
    POST: function POST(url, body, headers) {
      // Basic POST request in CORS mode;
      // console.log(`POST ${url} ${JSON.stringify(body)}`);
      return fetch(
        url,
        {
          method: 'POST',
          mode: 'cors',
          headers: {
            ...headers,
            'content-type': 'application/json',
          },
          body: JSON.stringify(body),
        },
      );
    },
  
    assertParse: function(response) {
      if (!response.ok) return response.text().then(text => { throw `[${response.status}] ${text}` });
      return response.json();
    }
  
  };
  
  export default Http;