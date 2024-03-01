import useSWR from "swr";

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
  const { data, error } = useSWR<Game[], Error>(
    "http://127.0.0.1:8080/games/",
    (url: string) => fetch(url).then((res) => res.json()),
  );

  return (
    <>
      {error ? (
        <span className="text-white">{error.message}</span>
      ) : (
        <ul>
          {data &&
            data.map((game: Game) => (
              <li key={crypto.randomUUID()} className="grid place-items-center">
                <img src={game.header_image} alt="logo" />
                <div className="text-white">{game.name}</div>
              </li>
            ))}
        </ul>
      )}
    </>
  );
}
