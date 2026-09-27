from dataclasses import dataclass

@dataclass
class MediaItem:
    id: int
    title: str
    genre: str
    platform: str
    status: str = "Plan to Watch"
    rating: float = None
    progress: int = 0

    def markCompleted(self):
        self.status = "Completed"


@dataclass
class Movie(MediaItem):
    duration: int = 0

    def calculateWatchTime(self):
        if self.status == "Completed":
            return self.duration
        return 0


@dataclass
class Series(MediaItem):
    total_episodes: int = 0
    episodes_runtime: int = 45

    def calculateWatchTime(self):
        return self.progress * self.episodes_runtime

    def progressPercentage(self):
        if self.total_episodes == 0:
            return 0

        return (self.progress / self.total_episodes) * 100


m1 = Movie(1, 'Dhurandhar', 'Action', 'Netflix')
m2 = Movie(7, 'Sholay', 'Drama', 'Prime')
print(m1.title)
m1.duration = 150
m1.markCompleted()
print(m1.calculateWatchTime())
print()
print(m2.title)
m2.rating = 4
print(m2.calculateWatchTime())

s1 = Series(10, 'Stranger Things', 'Sci-Fi', 'Netflix', total_episodes=34)
print()
print(s1.title)

s1.progress = 10

print("Total Series Watch Time:", s1.calculateWatchTime(), "minutes")
print("Progress Percentage:", s1.progressPercentage(), "%")