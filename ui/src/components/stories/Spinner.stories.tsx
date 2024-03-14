import Spinner from "../Spinner";
import { StoryObj, Meta } from "@storybook/react";

export default {
  component: Spinner,
  title: "Loader",
  tags: ["autodocs"],
  parameters: {
    layout: "centered",
  },
} satisfies Meta<typeof Spinner>;

type Story = StoryObj<typeof Spinner>;

export const Default: Story = {};
