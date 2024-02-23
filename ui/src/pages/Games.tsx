import React from "react";
import { useEffect, useState } from "react";

export default function Games() {
  const [data, setData] = useState<Array<unknown>>([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8080/games/", { method: "GET" })
      .then(
        (response) => {
          if (response.ok) {
            return response.json();
          }
          throw response;
        },
        (error) => {
          console.log(error);
        },
      )
      .then((data) => {
        setData(data);
      });
  }, []);
  return (
    <>
      <h1>Games</h1>
      <ul className="games">
        {data &&
          data.map((game: unknown) => (
            <li key={crypto.randomUUID()}>
              <img
                src={(game as { header_image: string }).header_image}
                alt="logo"
              />
              <div className="game">
                <div className="game-name">
                  {(game as { name: string }).name}
                </div>
              </div>
            </li>
          ))}
      </ul>
    </>
  );
}
