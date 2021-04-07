interface Match {
  localTeam: number;
  visitorTeam: number;
  localScore: number;
  visitorScore: number;
  date: Date;
  tournamentDate: number;
}

const matches6: Match[] = [
  {
    localTeam: 16,
    visitorTeam: 10,
    localScore: 1,
    visitorScore: 1,
    date: new Date(2021, 3, 1, 17, 30),
    tournamentDate: 6,
  },
  {
    localTeam: 13,
    visitorTeam: 6,
    localScore: 2,
    visitorScore: 3,
    date: new Date(2021, 3, 1, 20, 0),
    tournamentDate: 6,
  },
  {
    localTeam: 4,
    visitorTeam: 5,
    localScore: 1,
    visitorScore: 1,
    date: new Date(2021, 3, 3, 12, 15),
    tournamentDate: 6,
  },
  {
    localTeam: 9,
    visitorTeam: 12,
    localScore: 0,
    visitorScore: 0,
    date: new Date(2021, 3, 3, 14, 30),
    tournamentDate: 6,
  },
  {
    localTeam: 3,
    visitorTeam: 8,
    localScore: 2,
    visitorScore: 2,
    date: new Date(2021, 3, 3, 17, 0),
    tournamentDate: 6,
  },
  {
    localTeam: 14,
    visitorTeam: 11,
    localScore: 0,
    visitorScore: 1,
    date: new Date(2021, 3, 4, 12, 15),
    tournamentDate: 6,
  },
  {
    localTeam: 1,
    visitorTeam: 2,
    localScore: 1,
    visitorScore: 3,
    date: new Date(2021, 3, 4, 14, 30),
    tournamentDate: 6,
  },
  {
    localTeam: 15,
    visitorTeam: 7,
    localScore: 3,
    visitorScore: 0,
    date: new Date(2021, 3, 4, 17, 0),
    tournamentDate: 6,
  },
];

console.log(JSON.stringify(matches6));
