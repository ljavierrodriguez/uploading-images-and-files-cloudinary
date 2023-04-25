import React, { useEffect, useState } from 'react'

const App = () => {

  const [image, setImage] = useState(null);
  const [title, setTitle] = useState("");
  const [uploads, setUploads] = useState(null);

  const [result, setResult] = useState(null);

  useEffect(() => {
    getUploads('https://5000-ljavierrodr-uploadingim-c7tumx0fh0o.ws-us95.gitpod.io/uploads');
  }, [])

  const handleUploadImages = e => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('title', title);
    formData.append('image', image);
    formData.append('type_upload', "video")

    fetchUploadImages('https://5000-ljavierrodr-uploadingim-c7tumx0fh0o.ws-us95.gitpod.io/upload', formData);

  }

  const fetchUploadImages = (url, data) => {
    fetch(url, {
      method: 'POST',
      body: data,
      /* headers: {
        'Authorization': 'Bearer <token>'
      } */
    })
      .then(resp => resp.json())
      .then(data => {
        if (data.msg) {
          console.log(data.msg);
        } else {
          setResult(data)
        }
      })
  }

  const getUploads = (url) => {
    fetch(url).then(resp => resp.json()).then(data => setUploads(data));
  }

  return (
    <>
      <form onSubmit={handleUploadImages}>
        <input type="file" name="image" id="image" onChange={(e) => setImage(e.target.files[0])} />
        <input type="text" name="title" id="title" onChange={(e) => setTitle(e.target.value)} placeholder='Ingrese titulo' />
        <button>Upload</button>
      </form>

      {
        !!result && (
          <>
            <img src={result.image} width={200} height={200} />
            <h3>{result.title}</h3>
          </>
        )
      }

      <ul>
        {
          !!uploads &&
          uploads.length > 0 &&
          uploads.map((item) => {
            console.log(item.type_upload)
            return (
              <li key={item.id}>
                {
                  item.type_upload === 'image' ?
                    (
                      <>
                        <img src={item.image} width={100} height={100} />
                        <h4>{item.title}</h4>
                      </>
                    ) : (
                      <>
                        <audio src={item.image} controls />
                        <h4>{item.title}</h4>
                      </>
                    )
                }
              </li>
            )
          })
        }
      </ul>

    </>
  )
}

export default App