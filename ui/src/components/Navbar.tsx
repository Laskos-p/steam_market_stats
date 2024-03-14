import { Link } from "@tanstack/react-router";

const Navbar = () => {
  return (
    <div className="flex items-center justify-between bg-primary p-4 ring-[1rem] ring-secondary">
      <Link to="/">
        <h1>Steam Market</h1>
      </Link>
      <nav>
        <ul className="flex h-full gap-4">
          {(
            [
              ["/", "Home"],
              ["/items", "Items"],
            ] as const
          ).map(([to, label]) => (
            <li key={to}>
              <Link
                to={to}
                className="grid aspect-video items-center px-4 hover:bg-[#777] focus-visible:bg-[#777]"
                activeProps={{
                  className: "bg-[#555]",
                }}
              >
                {label}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
};

export default Navbar;
