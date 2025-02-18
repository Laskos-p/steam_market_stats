import { useEffect, useState } from "react";

interface Game {
  appid: number;
  name: string;
  header_image: string;
  listed_unique_items: number;
  all_unique_items: number;
  number_of_listings: number;
  value_of_listings: number;
}

export default function Games() {
  const [data, setData] = useState<Game[]>([]);
  const [error, setError] = useState<string | null>(null);

  async function fetchItems() {
    const response = await fetch("http://127.0.0.1:8080/games/");
    return (await response.json()) as Game[];
  }

  useEffect(() => {
    fetchItems()
      .then((data) => setData(data))
      .catch((error: Error) => {
        setError(error.message);
      });
  }, []);

  return (
    <>
      <h1>Games</h1>
      {error || (
        <ul className="games">
          {data &&
            data.map((game: Game) => (
              <li key={crypto.randomUUID()}>
                <img src={game.header_image} alt="logo" />
                <div className="game">
                  <div className="game-name">{game.name}</div>
                </div>
              </li>
            ))}
        </ul>
      )}
    </>
  );
}
