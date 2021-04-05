import * as Papa from "papaparse";
import * as fs from "fs/promises";
import { Parser } from "json2csv";

const FECHA = 5;

type Tweet = {
  id: string;
  text: string;
  created_at: string;
  user_id: string;
  user_name: string;
  user_screen_name: string;
  favorite_count: string;
  retweet_count: string;
  source: string;
  place: string;
  polarity: "0" | "1";
};

function calcRelevance(
  favorites: number,
  retweets: number,
  tweetCount: number
) {
  const ALPHA = 0.4;
  const BETA = 0.6;

  return (ALPHA * favorites + BETA * retweets) / tweetCount;
}

async function main(fileName) {
  const str = await fs.readFile(`tweets_2/${fileName}.csv`, {
    encoding: "utf-8",
  });
  const { data } = Papa.parse<Tweet>(str, { delimiter: ",", header: true });

  const tweets = data
    .map(({ text, ...tweet }) => ({
      ...tweet,
      favorite_count: +tweet.favorite_count,
      retweet_count: +tweet.retweet_count,
    }))
    .reduce((arr, tweet, _, array) => {
      return [
        ...arr,
        {
          ...tweet,
          relevance: calcRelevance(
            tweet.favorite_count,
            tweet.retweet_count,
            array.length
          ),
        },
      ];
    }, []);
  tweets.pop();

  const parser = new Parser({
    fields: [
      "id",
      "created_at",
      "user_id",
      "user_name",
      "user_screen_name",
      "favorite_count",
      "retweet_count",
      "source",
      "place",
      "polarity",
      "relevance",
    ],
  });
  const csv = parser.parse(tweets);
  await fs.writeFile(`tweets_3/${fileName}.csv`, csv, "utf-8");
  console.log(`${fileName} saved`);
}

(async function () {
  for (let i = 1; i <= 16; i++) {
    const fileName = `equipo_${i}_fecha_${FECHA}`;
    await main(fileName);
  }
})();
